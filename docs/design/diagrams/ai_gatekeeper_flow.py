"""
BetterSelf -- AI Accountability Gatekeeper Flow Diagram
Shows the decision flow when a user tries to override a focus session.

Usage:
    pip install graphviz
    python ai_gatekeeper_flow.py
"""

import os
import graphviz

script_dir = os.path.dirname(os.path.abspath(__file__))

dot = graphviz.Digraph(
    "BetterSelf - AI Gatekeeper Flow",
    format="png",
    engine="dot",
    graph_attr={
        "rankdir": "TB",
        "bgcolor": "white",
        "fontsize": "14",
        "pad": "0.5",
        "nodesep": "0.6",
        "ranksep": "0.7",
        "dpi": "150",
        "label": "BetterSelf - AI Accountability Gatekeeper (Strict Mode Override Flow)",
        "labelloc": "t",
        "fontname": "Helvetica-Bold",
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
        "fontsize": "10",
    },
)

dot.node("blocked", "User encounters\nblocked app shield", fillcolor="#FFCDD2", pencolor="#C62828")
dot.node("override_tap", "User taps\n\"Override\" button", fillcolor="#FFCDD2", pencolor="#C62828")
dot.node("ai_challenge", "AI asks:\n\"Why do you need\nto stop focusing?\"", fillcolor="#B39DDB", pencolor="#7E57C2", shape="box")
dot.node("user_speaks", "User explains\ntheir reason\n(voice or text)", fillcolor="#E3F2FD", pencolor="#1565C0")
dot.node("ai_evaluates", "AI evaluates\nreason using\nBedrock LLM", fillcolor="#B39DDB", pencolor="#7E57C2")

dot.node("decision", "Legitimate\nreason?", fillcolor="#FFF9C4", pencolor="#F57F17", shape="diamond")

dot.node("cooldown", "5-minute\ncooldown timer\nstarts", fillcolor="#C8E6C9", pencolor="#43A047")
dot.node("unlocked", "Session ended\nsuccessfully", fillcolor="#A5D6A7", pencolor="#2E7D32")

dot.node("denied", "AI encourages\nuser to continue\n(motivational message)", fillcolor="#FFCC80", pencolor="#EF6C00")
dot.node("retry", "User can try\nagain in 15 min", fillcolor="#FFCDD2", pencolor="#C62828")

dot.node("examples_yes", "Legitimate:\n• Genuine emergency\n• Urgent work need\n• Scheduled break\n• Safety concern", fillcolor="#C8E6C9", pencolor="#43A047", shape="note")
dot.node("examples_no", "Not Legitimate:\n• Boredom\n• \"Just checking\"\n• Social media FOMO\n• Vague reasons", fillcolor="#FFCDD2", pencolor="#C62828", shape="note")

dot.edge("blocked", "override_tap")
dot.edge("override_tap", "ai_challenge", color="#7E57C2", penwidth="2")
dot.edge("ai_challenge", "user_speaks", color="#1565C0", penwidth="2")
dot.edge("user_speaks", "ai_evaluates", color="#7E57C2", penwidth="2")
dot.edge("ai_evaluates", "decision", color="#F57F17", penwidth="2")

dot.edge("decision", "cooldown", label="  Yes  ", color="#43A047", penwidth="2")
dot.edge("cooldown", "unlocked", color="#43A047", penwidth="2")

dot.edge("decision", "denied", label="  No  ", color="#E53935", penwidth="2")
dot.edge("denied", "retry", color="#E53935", penwidth="2")
dot.edge("retry", "ai_challenge", label="  After 15 min  ", style="dashed", color="#999999")

dot.edge("decision", "examples_yes", style="dotted", color="#43A047", arrowhead="none")
dot.edge("decision", "examples_no", style="dotted", color="#E53935", arrowhead="none")

dot.render(os.path.join(script_dir, "ai_gatekeeper_flow"), cleanup=True)
