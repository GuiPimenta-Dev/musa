from infra.services import Services

class MusaConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Musa",
            path="./functions/musa",
            description="A simple hello word",
            
        )

        services.api_gateway.create_endpoint("GET", "/musa", function, public=True)

            