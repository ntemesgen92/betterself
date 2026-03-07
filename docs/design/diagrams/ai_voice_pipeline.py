"""
BetterSelf -- AI & Voice Processing Pipeline Diagram
Shows the end-to-end flow from voice input to AI response.

Usage:
    pip install diagrams
    python ai_voice_pipeline.py
"""

import os
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.ml import Transcribe
from diagrams.aws.storage import S3
from diagrams.generic.device import Mobile

script_dir = os.path.dirname(os.path.abspath(__file__))

graph_attr = {
    "fontsize": "28",
    "bgcolor": "white",
    "pad": "0.8",
    "nodesep": "0.6",
    "ranksep": "1.0",
    "dpi": "150",
}

with Diagram(
    "BetterSelf - AI & Voice Processing Pipeline",
    filename=os.path.join(script_dir, "ai_voice_pipeline"),
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    outformat="png",
):

    with Cluster("iOS App", graph_attr={"style": "rounded", "bgcolor": "#E3F2FD"}):
        mic = Mobile("User Taps\nMic Button")
        speech_display = Mobile("Display\nTranscript")
        audio_play = Mobile("Play Audio\nResponse")
        action_card = Mobile("Show Action\nConfirmation")

    with Cluster("Free Tier Path", graph_attr={"style": "rounded", "bgcolor": "#C8E6C9"}):
        apple_speech = Mobile("Apple Speech\nFramework\n(On-Device STT)")
        apple_tts = Mobile("AVSpeechSynthesizer\n(On-Device TTS)")

    with Cluster("Premium Tier Path", graph_attr={"style": "rounded", "bgcolor": "#FFF3CD"}):
        s3_upload = S3("S3 Temp\nAudio Upload")
        transcribe = Transcribe("AWS Transcribe\n(Streaming STT)")
        polly = Lambda("AWS Polly\n(Neural TTS)\nJoanna Voice")
        s3_response = S3("S3 Presigned\nAudio URL")

    with Cluster("AI Processing (Both Tiers)", graph_attr={"style": "rounded", "bgcolor": "#F3E5F5"}):
        context_builder = Lambda("Context Builder\n(Schedule + Tasks\n+ Last 10 Messages)")
        bedrock = Lambda("AWS Bedrock\n(Claude 3 Sonnet)\nSecretary Persona")
        action_parser = Lambda("Action Parser\n(JSON Extraction)")

    with Cluster("Action Execution", graph_attr={"style": "rounded", "bgcolor": "#FBE9E7"}):
        calendar_action = Dynamodb("Create/Update\nCalendar Event")
        task_action = Dynamodb("Create/Update\nTask")
        blocking_action = Dynamodb("Update Blocking\nProfile")
        briefing_action = Lambda("Generate\nDaily Briefing")

    with Cluster("Conversation Storage", graph_attr={"style": "rounded", "bgcolor": "#E0F2F1"}):
        conversation_db = Dynamodb("DynamoDB\nAI Conversations\n(TTL: 90 days)")

    # Free tier flow
    mic >> Edge(label="1. Record\nAudio", color="purple") >> apple_speech
    apple_speech >> Edge(label="2. Transcript\n(text)", color="green") >> speech_display
    apple_speech >> Edge(label="3. Send text\nto API", color="green") >> context_builder

    # Premium tier flow
    mic >> Edge(label="1. Upload\nAudio", color="orange", style="dashed") >> s3_upload
    s3_upload >> Edge(label="2. Transcribe", color="orange") >> transcribe
    transcribe >> Edge(label="3. Transcript", color="orange") >> context_builder

    # Shared AI flow
    context_builder >> Edge(label="4. System Prompt\n+ Context\n+ User Message", color="purple") >> bedrock
    bedrock >> Edge(label="5. AI Response\n+ Action JSON", color="purple") >> action_parser

    # Action execution
    action_parser >> Edge(label="create_event", color="blue", style="dashed") >> calendar_action
    action_parser >> Edge(label="create_task", color="blue", style="dashed") >> task_action
    action_parser >> Edge(label="update_profile", color="red", style="dashed") >> blocking_action
    action_parser >> Edge(label="gen_briefing", color="teal", style="dashed") >> briefing_action

    # Response back to user
    action_parser >> Edge(label="6. Response\nText", color="green") >> action_card

    # Free tier TTS
    action_parser >> Edge(label="7a. Free:\nLocal TTS", color="green", style="dashed") >> apple_tts
    apple_tts >> Edge(label="8a. Play", color="green") >> audio_play

    # Premium tier TTS
    action_parser >> Edge(label="7b. Premium:\nPolly TTS", color="orange", style="dashed") >> polly
    polly >> Edge(label="8b. Audio", color="orange") >> s3_response
    s3_response >> Edge(label="9b. Stream", color="orange") >> audio_play

    # Store conversation
    bedrock >> Edge(label="Log", style="dashed", color="gray") >> conversation_db
