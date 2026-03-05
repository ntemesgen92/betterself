"""
BetterSelf -- Full System Architecture Diagram
Generates a comprehensive PNG of the complete system.

Usage:
    pip install diagrams
    python full_architecture.py
"""

import os
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Aurora, Dynamodb
from diagrams.aws.integration import SNS, Eventbridge
from diagrams.aws.ml import Transcribe
from diagrams.aws.network import APIGateway, VPC as VPCIcon, NATGateway, InternetGateway
from diagrams.aws.security import Cognito, WAF, SecretsManager
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import User
from diagrams.generic.device import Mobile

script_dir = os.path.dirname(os.path.abspath(__file__))
icons_dir = os.path.join(script_dir, "icons")
os.makedirs(icons_dir, exist_ok=True)

graph_attr = {
    "fontsize": "32",
    "bgcolor": "white",
    "pad": "1.0",
    "nodesep": "0.6",
    "ranksep": "1.0",
    "dpi": "150",
}

with Diagram(
    "BetterSelf - Full System Architecture",
    filename=os.path.join(script_dir, "full_architecture"),
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat="png",
):
    user = User("Productivity-Focused\nUser")

    with Cluster("iOS App (Swift + SwiftUI)", graph_attr={"style": "rounded", "bgcolor": "#E3F2FD"}):
        app = Mobile("BetterSelf\niOS App")

        with Cluster("Core Features", graph_attr={"style": "rounded", "bgcolor": "#BBDEFB"}):
            voice_ui = Mobile("Voice-First\nAI Chat")
            focus_ui = Mobile("Focus Mode\n(FamilyControls)")
            calendar_ui = Mobile("Calendar\nManager")

        with Cluster("System Integrations", graph_attr={"style": "rounded", "bgcolor": "#90CAF9"}):
            widgets = Mobile("WidgetKit\n+ Live Activities")
            siri = Mobile("Siri Shortcuts\n(App Intents)")
            speech_local = Mobile("Apple Speech\n(On-Device STT)")

    with Cluster("AWS Cloud", graph_attr={"style": "rounded", "bgcolor": "#FFF8E1"}):

        with Cluster("Edge & Auth", graph_attr={"style": "rounded", "bgcolor": "#FFEBEE"}):
            waf = WAF("Web Application\nFirewall (WAF)")
            cognito = Cognito("Cognito User Pool\n(Email + Apple\n+ Google Sign-In)")

        with Cluster("VPC: 10.0.0.0/16", graph_attr={"style": "rounded", "bgcolor": "#E8EAF6"}):

            with Cluster("Public Subnets", graph_attr={"style": "rounded", "bgcolor": "#C8E6C9"}):
                igw = InternetGateway("Internet\nGateway")
                api_gw = APIGateway("API Gateway\n(HTTP API)")
                nat = NATGateway("NAT\nGateway")

            with Cluster("Private Subnets", graph_attr={"style": "rounded", "bgcolor": "#F3E5F5"}):
                with Cluster("Lambda SG\n(Outbound: Internet + DB)", graph_attr={"style": "dashed", "bgcolor": "#CE93D8", "pencolor": "#6A1B9A"}):
                    lambda_fn = Lambda("FastAPI Lambda\n(Python 3.12)\n256 MB / 30s timeout")

                with Cluster("Aurora SG\n(Inbound: 5432 from Lambda SG)", graph_attr={"style": "dashed", "bgcolor": "#CE93D8", "pencolor": "#6A1B9A"}):
                    aurora = Aurora("Calendar & Tasks DB\n(Aurora Serverless v2\nPostgreSQL 15)\n0.5-4 ACU")

        with Cluster("AI & Voice Pipeline", graph_attr={"style": "rounded", "bgcolor": "#E0F7FA"}):
            bedrock = Lambda("AWS Bedrock\n(Claude 3 Sonnet)\nAI Secretary")
            transcribe = Transcribe("AWS Transcribe\n(Premium STT)")
            polly = Lambda("AWS Polly\n(Neural TTS)\nJoanna Voice")

        with Cluster("Data Stores", graph_attr={"style": "rounded", "bgcolor": "#FBE9E7"}):
            dynamodb = Dynamodb("DynamoDB\n(Users, Profiles,\nSessions, Chats)\nOn-Demand + PITR")
            s3 = S3("S3\n(Audio Temp\n+ Assets)")

        with Cluster("Notifications & Scheduling", graph_attr={"style": "rounded", "bgcolor": "#E0F2F1"}):
            sns = SNS("SNS\n(Push via APNs)")
            eventbridge = Eventbridge("EventBridge\n(Daily Briefing\nCron Jobs)")

        secrets = SecretsManager("Secrets Manager\n(DB Credentials)")
        cloudwatch = Cloudwatch("CloudWatch\n(Logs + Metrics)")

    with Cluster("External Services", graph_attr={"style": "rounded", "bgcolor": "#ECEFF1"}):
        apple_calendar = Mobile("Apple Calendar\n(EventKit)")
        google_calendar = Mobile("Google Calendar\n(REST API v3)")

    user >> app

    voice_ui >> Edge(label="Push-to-Talk\nAudio", color="purple") >> app
    focus_ui >> Edge(label="FamilyControls\nShield Apps", color="red", style="dashed") >> app
    calendar_ui >> Edge(label="EventKit +\nGoogle API", color="blue", style="dashed") >> app
    siri >> Edge(label="Voice\nCommands", color="gray", style="dashed") >> app

    app >> Edge(label="REST API\n(Bearer JWT)", color="darkgreen") >> waf
    app >> Edge(label="Auth Flows", color="orange") >> cognito
    waf >> Edge(label="Rate-limited\nTraffic", color="darkgreen") >> igw
    igw >> api_gw
    api_gw >> Edge(label="Cognito\nAuthorizer") >> cognito
    api_gw >> lambda_fn

    lambda_fn >> Edge(label="SQL\n(Calendar, Tasks,\nHabits)", color="blue") >> aurora
    lambda_fn >> Edge(label="NoSQL\n(Users, Sessions,\nConversations)", color="orange") >> dynamodb
    lambda_fn >> Edge(label="AI Chat +\nSchedule\nOptimization", color="purple") >> bedrock
    lambda_fn >> Edge(label="Premium\nSTT", color="teal") >> transcribe
    lambda_fn >> Edge(label="TTS\nResponse", color="teal") >> polly
    lambda_fn >> Edge(label="Audio\nStorage", color="gray") >> s3
    lambda_fn >> Edge(label="DB Creds", style="dashed", color="gray") >> secrets
    lambda_fn >> Edge(label="Logs", style="dashed", color="gray") >> cloudwatch

    lambda_fn >> Edge(label="Push\nNotifications", color="teal") >> sns
    sns >> Edge(label="APNs\nPush", color="orange") >> app
    eventbridge >> Edge(label="Daily Briefing\n+ Reminders", color="gray") >> lambda_fn

    app >> Edge(label="Read/Write\nEvents", color="blue", style="dashed") >> apple_calendar
    app >> Edge(label="OAuth +\nSync", color="red", style="dashed") >> google_calendar

    speech_local >> Edge(label="Free Tier\nOn-Device STT", color="gray", style="dashed") >> voice_ui
