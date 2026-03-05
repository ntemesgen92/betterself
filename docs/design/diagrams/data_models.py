"""
BetterSelf -- Data Model ER Diagram
Shows entity relationships for all data models.

Usage:
    pip install graphviz
    python data_models.py
"""

import os
import graphviz

script_dir = os.path.dirname(os.path.abspath(__file__))

dot = graphviz.Digraph(
    "BetterSelf - Data Models",
    format="png",
    engine="dot",
    graph_attr={
        "rankdir": "LR",
        "bgcolor": "white",
        "fontsize": "14",
        "pad": "0.5",
        "nodesep": "0.8",
        "ranksep": "1.5",
        "dpi": "150",
        "label": "BetterSelf - Data Model (ER Diagram)",
        "labelloc": "t",
        "fontname": "Helvetica-Bold",
    },
    node_attr={
        "shape": "plaintext",
        "fontname": "Helvetica",
        "fontsize": "11",
    },
    edge_attr={
        "fontname": "Helvetica",
        "fontsize": "10",
    },
)

def entity_table(name, color, fields):
    """Generate an HTML-like label for an entity."""
    rows = ""
    for field_name, field_type, constraint in fields:
        badge = ""
        if constraint == "PK":
            badge = ' <font color="#D32F2F"><b>PK</b></font>'
        elif constraint == "FK":
            badge = ' <font color="#1565C0"><b>FK</b></font>'
        rows += f'<tr><td align="left"><b>{field_name}</b></td><td align="left">{field_type}{badge}</td></tr>\n'

    return f'''<
    <table border="0" cellborder="1" cellspacing="0" cellpadding="6">
        <tr><td colspan="2" bgcolor="{color}"><b><font color="white" point-size="13">{name}</font></b></td></tr>
        {rows}
    </table>
    >'''

dot.node("User", entity_table("User", "#5B8DEF", [
    ("id", "string", "PK"),
    ("email", "string", ""),
    ("name", "string", ""),
    ("auth_provider", "string", ""),
    ("subscription_tier", "string", ""),
    ("created_at", "datetime", ""),
    ("preferences", "jsonb", ""),
]))

dot.node("BlockingProfile", entity_table("BlockingProfile", "#E57373", [
    ("id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("name", "string", ""),
    ("mode", "string", ""),
    ("blocked_apps", "jsonb", ""),
    ("allowed_apps", "jsonb", ""),
    ("schedule", "jsonb", ""),
    ("is_active", "boolean", ""),
    ("strict_mode", "boolean", ""),
]))

dot.node("BlockingSession", entity_table("BlockingSession", "#EF5350", [
    ("id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("profile_id", "string", "FK"),
    ("start_time", "datetime", ""),
    ("end_time", "datetime", ""),
    ("override_attempts", "int", ""),
    ("completed", "boolean", ""),
]))

dot.node("CalendarEvent", entity_table("CalendarEvent", "#4ECDC4", [
    ("id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("external_id", "string", ""),
    ("source", "string", ""),
    ("title", "string", ""),
    ("start_time", "datetime", ""),
    ("end_time", "datetime", ""),
    ("location", "string", ""),
    ("ai_created", "boolean", ""),
    ("recurrence", "jsonb", ""),
]))

dot.node("Task", entity_table("Task", "#9B8FE8", [
    ("id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("title", "string", ""),
    ("priority", "string", ""),
    ("status", "string", ""),
    ("due_date", "datetime", ""),
    ("completed_at", "datetime", ""),
]))

dot.node("Habit", entity_table("Habit", "#FFB74D", [
    ("id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("name", "string", ""),
    ("frequency", "string", ""),
    ("tracking_data", "jsonb", ""),
    ("current_streak", "int", ""),
]))

dot.node("AIConversation", entity_table("AIConversation", "#7E57C2", [
    ("id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("timestamp", "datetime", ""),
    ("role", "string", ""),
    ("content", "text", ""),
    ("action_type", "string", ""),
    ("action_data", "jsonb", ""),
]))

dot.node("DailyBriefing", entity_table("DailyBriefing", "#26A69A", [
    ("id", "string", "PK"),
    ("user_id", "string", "FK"),
    ("briefing_date", "date", ""),
    ("schedule_summary", "jsonb", ""),
    ("tasks_summary", "jsonb", ""),
    ("focus_summary", "jsonb", ""),
    ("ai_recommendations", "text", ""),
]))

dot.edge("User", "BlockingProfile", label="  1:N  ", color="#E57373", penwidth="2")
dot.edge("User", "BlockingSession", label="  1:N  ", color="#EF5350", penwidth="2")
dot.edge("User", "CalendarEvent", label="  1:N  ", color="#4ECDC4", penwidth="2")
dot.edge("User", "Task", label="  1:N  ", color="#9B8FE8", penwidth="2")
dot.edge("User", "Habit", label="  1:N  ", color="#FFB74D", penwidth="2")
dot.edge("User", "AIConversation", label="  1:N  ", color="#7E57C2", penwidth="2")
dot.edge("User", "DailyBriefing", label="  1:N  ", color="#26A69A", penwidth="2")
dot.edge("BlockingProfile", "BlockingSession", label="  1:N  ", color="#EF5350", style="dashed", penwidth="2")

dot.render(os.path.join(script_dir, "data_models"), cleanup=True)
