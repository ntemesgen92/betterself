"""
BetterSelf -- Security Groups & IAM Roles Diagram
Shows security group boundaries and IAM role permissions.

Usage:
    pip install diagrams
    python security_groups.py
"""

import os
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Aurora, Dynamodb
from diagrams.aws.network import APIGateway
from diagrams.aws.security import Cognito, IAMRole, WAF, SecretsManager
from diagrams.aws.storage import S3
from diagrams.aws.integration import SNS
from diagrams.aws.management import Cloudwatch

script_dir = os.path.dirname(os.path.abspath(__file__))

graph_attr = {
    "fontsize": "28",
    "bgcolor": "white",
    "pad": "0.8",
    "nodesep": "0.8",
    "ranksep": "1.0",
    "dpi": "150",
}

with Diagram(
    "BetterSelf - Security Groups & IAM Roles",
    filename=os.path.join(script_dir, "security_groups"),
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    outformat="png",
):
    with Cluster("Security Groups", graph_attr={"style": "rounded", "bgcolor": "#FDECEA"}):
        with Cluster("WAF + API Gateway\nInbound: HTTPS from Internet"):
            waf = WAF("Web Application\nFirewall (WAF)")
            api_gw = APIGateway("API Gateway\n(HTTP API)")

        with Cluster("Lambda SG\nInbound: From API Gateway\nOutbound: 5432, 443"):
            lambda_fn = Lambda("FastAPI Lambda\n(Python 3.12)")

        with Cluster("Aurora SG\nInbound: 5432 from Lambda SG only"):
            aurora = Aurora("Aurora Serverless v2\n(PostgreSQL 15)")

    waf >> Edge(label="Filtered\nTraffic") >> api_gw
    api_gw >> Edge(label="Invoke", color="darkgreen") >> lambda_fn
    lambda_fn >> Edge(label="TCP 5432", color="blue") >> aurora

    with Cluster("Lambda Execution Role", graph_attr={"style": "rounded", "bgcolor": "#E8F0FE"}):
        exec_role = IAMRole("Lambda\nExecution Role")

    with Cluster("Lambda Task Permissions", graph_attr={"style": "rounded", "bgcolor": "#E8F0FE"}):
        task_role = IAMRole("Lambda\nTask Role")

    with Cluster("AWS Services (Task Role Access)", graph_attr={"style": "rounded", "bgcolor": "#F3E5F5"}):
        dynamodb = Dynamodb("DynamoDB\nTables")
        s3 = S3("S3 Audio\nBucket")
        sns = SNS("SNS Push\nNotifications")
        secrets = SecretsManager("Secrets\nManager")
        logs = Cloudwatch("CloudWatch\nLogs")

    exec_role >> Edge(label="Pull Layer\n+ Write Logs", style="dashed") >> logs

    task_role >> Edge(label="CRUD\n(Users, Sessions,\nProfiles, Chats)", style="dashed", color="orange") >> dynamodb
    task_role >> Edge(label="Read/Write\nAudio", style="dashed", color="gray") >> s3
    task_role >> Edge(label="Publish\nPush", style="dashed", color="teal") >> sns
    task_role >> Edge(label="Get DB\nCredentials", style="dashed", color="red") >> secrets

    with Cluster("AI Service Permissions", graph_attr={"style": "rounded", "bgcolor": "#E0F7FA"}):
        bedrock_role = IAMRole("Bedrock\nInvoke Role")
        voice_role = IAMRole("Transcribe +\nPolly Role")

    bedrock_role >> Edge(label="bedrock:InvokeModel\n(Claude 3)", style="dashed", color="purple") >> lambda_fn
    voice_role >> Edge(label="transcribe:StartStream\npolly:SynthesizeSpeech", style="dashed", color="teal") >> lambda_fn
