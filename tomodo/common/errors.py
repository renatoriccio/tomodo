class EmptyDeployment(Exception):
    pass


class InvalidDeploymentType(Exception):
    def __init__(self, deployment_type: str = None):
        self.deployment_type = deployment_type
