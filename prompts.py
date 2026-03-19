def build_system_prompt(memories):
    memory_text = "\n".join(f"- {m}" for m in memories) if memories else "No past memory yet."
    
    return f"""You are a helpful study buddy assistant. You help users learn and understand topics deeply.

You have access to the user's past study history:
{memory_text}

Guidelines:
- Reference what the user has already learned when relevant
- Build on past knowledge instead of repeating basics
- Track their understanding and encourage progress
- At the end of each response, summarize what was just learned in one line starting with "📝 Learned:"
- Be encouraging and patient
"""

def build_memory_summary(conversation):
    return f"""Summarize the key topics and concepts learned in this conversation in 1-2 sentences. 
Be specific about what was understood and any areas of difficulty.

Conversation:
{conversation}

Summary:"""