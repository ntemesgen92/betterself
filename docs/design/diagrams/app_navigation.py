"""
BetterSelf -- App Navigation & Screen Flow Diagram
Shows the 3-tab structure and screen hierarchy.

Usage:
    pip install graphviz
    python app_navigation.py
"""

import os
import graphviz

script_dir = os.path.dirname(os.path.abspath(__file__))

dot = graphviz.Digraph(
    "BetterSelf - App Navigation",
    format="png",
    engine="dot",
    graph_attr={
        "rankdir": "TB",
        "bgcolor": "white",
        "fontsize": "14",
        "pad": "0.5",
        "nodesep": "0.5",
        "ranksep": "0.8",
        "dpi": "150",
        "label": "BetterSelf - App Navigation & Screen Flow",
        "labelloc": "t",
        "fontname": "Helvetica-Bold",
        "compound": "true",
    },
    node_attr={
        "fontname": "Helvetica",
        "fontsize": "11",
        "style": "filled,rounded",
        "shape": "box",
        "penwidth": "1.5",
    },
    edge_attr={
        "fontname": "Helvetica",
        "fontsize": "9",
        "color": "#666666",
    },
)

with dot.subgraph(name="cluster_tabbar") as c:
    c.attr(label="Tab Bar", style="rounded", bgcolor="#E3F2FD", fontname="Helvetica-Bold")
    c.node("home_tab", "Home", fillcolor="#5B8DEF", fontcolor="white", pencolor="#3D6BC7")
    c.node("focus_tab", "Focus", fillcolor="#E57373", fontcolor="white", pencolor="#C62828")
    c.node("calendar_tab", "Calendar", fillcolor="#4ECDC4", fontcolor="white", pencolor="#2E9E97")

with dot.subgraph(name="cluster_home") as c:
    c.attr(label="Home Tab", style="rounded", bgcolor="#E8F5E9", fontname="Helvetica-Bold")
    c.node("dashboard", "Dashboard\n(Summary Cards,\nGreeting, Quick Actions)", fillcolor="#C8E6C9", pencolor="#43A047")
    c.node("ai_chat", "AI Voice Chat\n(Push-to-Talk,\nConversation History)", fillcolor="#B39DDB", pencolor="#7E57C2")
    c.node("daily_briefing", "Daily Briefing\n(Schedule, Tasks,\nHabits, AI Insights)", fillcolor="#C8E6C9", pencolor="#43A047")
    c.node("task_list", "Task List\n(Priority Sorted,\nAI-Enhanced)", fillcolor="#C8E6C9", pencolor="#43A047")
    c.node("habit_tracker", "Habit Tracker\n(Streaks, Check-ins)", fillcolor="#C8E6C9", pencolor="#43A047")
    c.node("settings", "Settings\n(Account, Notifications,\nCalendars, Subscription)", fillcolor="#E0E0E0", pencolor="#757575")

with dot.subgraph(name="cluster_focus") as c:
    c.attr(label="Focus Tab", style="rounded", bgcolor="#FFEBEE", fontname="Helvetica-Bold")
    c.node("focus_home", "Focus Home\n(Active Session,\nScreen Time Stats)", fillcolor="#FFCDD2", pencolor="#E53935")
    c.node("profile_list", "Blocking Profiles\n(Saved Profiles Grid)", fillcolor="#FFCDD2", pencolor="#E53935")
    c.node("profile_editor", "Profile Editor\n(Apps, Schedule,\nMode, Strict Toggle)", fillcolor="#FFCDD2", pencolor="#E53935")
    c.node("app_picker", "App Picker\n(FamilyControls\nFamilyActivityPicker)", fillcolor="#FFCDD2", pencolor="#E53935")
    c.node("active_session", "Active Session\n(Timer, Breathing,\nOverride → AI Gatekeeper)", fillcolor="#EF9A9A", pencolor="#C62828")
    c.node("focus_history", "Focus History\n(Past Sessions,\nCompletion Stats)", fillcolor="#FFCDD2", pencolor="#E53935")

with dot.subgraph(name="cluster_calendar") as c:
    c.attr(label="Calendar Tab", style="rounded", bgcolor="#E0F7FA", fontname="Helvetica-Bold")
    c.node("calendar_view", "Calendar View\n(Month / Week / Day\nColor-Coded Events)", fillcolor="#B2EBF2", pencolor="#00838F")
    c.node("event_detail", "Event Detail\n(Title, Time, Source,\nEdit / Delete)", fillcolor="#B2EBF2", pencolor="#00838F")
    c.node("create_event", "Create Event\n(Form with Date,\nRecurrence, Source)", fillcolor="#B2EBF2", pencolor="#00838F")
    c.node("ai_schedule", "AI Optimizer\n(Schedule Suggestions,\nConflict Resolution)", fillcolor="#CE93D8", pencolor="#7B1FA2")

with dot.subgraph(name="cluster_onboarding") as c:
    c.attr(label="Onboarding (First Launch)", style="rounded,dashed", bgcolor="#FFF8E1", fontname="Helvetica-Bold")
    c.node("welcome", "Welcome", fillcolor="#FFF9C4", pencolor="#F57F17")
    c.node("goals", "Goals", fillcolor="#FFF9C4", pencolor="#F57F17")
    c.node("schedule_pref", "Schedule", fillcolor="#FFF9C4", pencolor="#F57F17")
    c.node("app_select", "App Selection", fillcolor="#FFF9C4", pencolor="#F57F17")
    c.node("calendar_connect", "Calendar\nConnection", fillcolor="#FFF9C4", pencolor="#F57F17")
    c.node("meet_ai", "Meet Your AI", fillcolor="#FFF9C4", pencolor="#F57F17")

# Tab connections
dot.edge("home_tab", "dashboard", penwidth="2", color="#5B8DEF")
dot.edge("focus_tab", "focus_home", penwidth="2", color="#E57373")
dot.edge("calendar_tab", "calendar_view", penwidth="2", color="#4ECDC4")

# Home tab navigation
dot.edge("dashboard", "ai_chat")
dot.edge("dashboard", "daily_briefing")
dot.edge("dashboard", "task_list")
dot.edge("dashboard", "habit_tracker")
dot.edge("dashboard", "settings")

# Focus tab navigation
dot.edge("focus_home", "profile_list")
dot.edge("profile_list", "profile_editor")
dot.edge("profile_editor", "app_picker")
dot.edge("focus_home", "active_session")
dot.edge("focus_home", "focus_history")

# Calendar tab navigation
dot.edge("calendar_view", "event_detail")
dot.edge("calendar_view", "create_event")
dot.edge("calendar_view", "ai_schedule")

# Onboarding flow
dot.edge("welcome", "goals", color="#F57F17")
dot.edge("goals", "schedule_pref", color="#F57F17")
dot.edge("schedule_pref", "app_select", color="#F57F17")
dot.edge("app_select", "calendar_connect", color="#F57F17")
dot.edge("calendar_connect", "meet_ai", color="#F57F17")
dot.edge("meet_ai", "dashboard", label="  Onboarding\n  Complete  ", color="#F57F17", style="dashed")

dot.render(os.path.join(script_dir, "app_navigation"), cleanup=True)
