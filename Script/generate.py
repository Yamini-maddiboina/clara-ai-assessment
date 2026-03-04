import os
import json

OUTPUT_DIR = "output"


def generate_prompt(memo):

    company = memo.get("company_name", "the company")
    hours = memo.get("business_hours", {})
    address = memo.get("office_address", "")

    prompt = f"""
You are a phone assistant for {company}.

Business Hours:
Days: {hours.get("days")}
Start: {hours.get("start")}
End: {hours.get("end")}
Timezone: {hours.get("timezone")}

Office Address:
{address}

Office Hours Flow:
1. Greet caller
2. Ask purpose of call
3. Collect name and phone number
4. Transfer call to agent
5. If transfer fails reassure caller

After Hours Flow:
1. Greet caller
2. Ask if emergency
3. Collect name, number and address
4. Attempt transfer
5. If transfer fails promise quick callback
"""

    return prompt.strip()


def generate_agents():

    for account_id in os.listdir(OUTPUT_DIR):

        memo_path = os.path.join(OUTPUT_DIR, account_id, "v1", "memo.json")

        if not os.path.exists(memo_path):
            continue

        with open(memo_path) as f:
            memo = json.load(f)

        agent = {
            "agent_name": memo["company_name"] + " Assistant",
            "voice_style": "professional and friendly",
            "system_prompt": generate_prompt(memo),

            "key_variables": {
                "business_hours": memo["business_hours"],
                "address": memo["office_address"]
            },

            "call_transfer_protocol": "Transfer call to human agent",
            "fallback_protocol": "If transfer fails take message and promise callback",
            "version": "v1"
        }

        agent_path = os.path.join(OUTPUT_DIR, account_id, "v1", "agent_spec.json")

        with open(agent_path, "w") as f:
            json.dump(agent, f, indent=4)

        print("Agent generated for:", account_id)


if __name__ == "__main__":
    generate_agents()