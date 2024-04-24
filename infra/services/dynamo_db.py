from aws_cdk import aws_dynamodb as dynamo_db
from aws_cdk import aws_iam as iam


class DynamoDB:
    def __init__(self, scope, context) -> None:

        # self.dynamo = dynamo_db.Table.from_table_arn(
        #     scope,
        #     "Dynamo",
        #     context.resources["arns"]["dynamo_arn"],
        # )
        ...

    @staticmethod
    def add_query_permission(table, function):
        function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:Query"],
                resources=[f"{table.table_arn}/index/*"],
            )
        )
