# -*- coding: utf-8 -*-

from d3m.container.dataset import Dataset
from d3m.metadata import hyperparams
from d3m.metadata.base import (
    PrimitiveAlgorithmType, PrimitiveFamily, PrimitiveInstallationType, PrimitiveMetadata)
from d3m.metadata.params import Params
from d3m.primitive_interfaces.base import CallResult
from d3m.primitive_interfaces.supervised_learning import SupervisedLearnerPrimitiveBase
from mlblocks import mlpipeline

Inputs = Dataset
Outputs = Dataset


class Hyperparams(hyperparams.Hyperparams):
    learner_params = hyperparams.Hyperparameter[dict](
        default={'1': 1},
        description='Arguments for the learner.',
        semantic_types=['https://metadata.datadrivendiscovery.org/types/TuningParameter']
    )


class Learner(SupervisedLearnerPrimitiveBase[Inputs, Outputs, Params, Hyperparams]):

    metadata = PrimitiveMetadata({
        'algorithm_types': [
            PrimitiveAlgorithmType.ADAPTIVE_ALGORITHM,
        ],
        'id': 'c1c54b03-717d-4e6b-b043-8fc93364b92e',
        'keywords': ['learner'],
        'name': "Learner",
        'primitive_family': PrimitiveFamily.LEARNER,
        'python_path': 'd3m.primitives.mit_primitives.Learner',
        'source': {
            'name': 'MIT_FeatureLabs',
        },
        'version': '0.0.3-dev',
        'installation': [{
            'type': PrimitiveInstallationType.PIP,
            'package_uri': (
                'git+https://github.com/HDI-Project/mit-primitives.git@'
                '{git_commit}#egg=mit-primitives'
            ).format(git_commit=utils.current_git_commit(os.path.dirname(__file__)))
        }],
    })

    def get_params(self) -> Params:
        return self.params

    def set_params(self, *, params: Params) -> None:
        if not hasattr(self, 'params'):
            self.params = params

        else:
            self.params.update(params)

    def set_training_data(self, *, inputs: Inputs, outputs: Outputs) -> None:
        self.inputs = inputs
        self.outputs = outputs

    def fit(self, *, timeout: float = None, iterations: int = None) -> CallResult[None]:
        learner_params = self.hyperparams['learner_params']
        learner = mlpipeline.MLPipeline(**learner_params)

        fit_params = self.params['fit_params']
        predict_params = self.params['predict_params']
        learner.fit(
            self.inputs,
            self.outputs,
            fit_params=fit_params,
            predict_params=predict_params,
        )

        self.params['learner'] = learner

        return CallResult(None)

    def produce(self, *, inputs: Inputs, timeout: float = None,
                iterations: int = None) -> CallResult[Outputs]:
        predict_params = self.params['predict_params']
        results = self.params['learner'].predict(inputs, predict_params=predict_params)

        return CallResult(results)

    def to_dict(self) -> dict:
        return self.params['learner'].to_dict()
