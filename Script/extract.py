import os
import json
import re

DATASET_DIR = "dataset"
OUTPUT_DIR = "output"


def extract_field(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""


def extract_services(text):
    services = []
    keywords = ["plumbing", "sprinkler", "hvac", "electrical", "repair"]

    for word in keywords:
        if word in text.lower():
            services.append(word)

    return list(set(services))


def process_demo_calls():

    for file in os.listdir(DATASET_DIR):

        if file.startswith("demo_call_") and file.endswith(".txt"):

            account_id = file.replace("demo_call_", "").replace(".txt", "")

            file_path = os.path.join(DATASET_DIR, file)

            with open(file_path, "r", encoding="utf-8") as f:
                transcript = f.read()

            memo = {
                "account_id": account_id,
                "company_name": extract_field(r"company name[:\-]?\s*(.*)", transcript),

                "business_hours": {
                    "days": extract_field(r"days[:\-]?\s*(.*)", transcript),
                    "start": extract_field(r"start[:\-]?\s*(.*)", transcript),
                    "end": extract_field(r"end[:\-]?\s*(.*)", transcript),
                    "timezone": extract_field(r"timezone[:\-]?\s*(.*)", transcript)
                },

                "office_address": extract_field(r"address[:\-]?\s*(.*)", transcript),

                "services_supported": extract_services(transcript),

                "emergency_definition": [],
                "emergency_routing_rules": "",
                "non_emergency_routing_rules": "",
                "call_transfer_rules": "",
                "integration_constraints": "",
                "after_hours_flow_summary": "",
                "office_hours_flow_summary": "",
                "questions_or_unknowns": [],
                "notes": ""
            }

            account_folder = os.path.join(OUTPUT_DIR, account_id, "v1")
            os.makedirs(account_folder, exist_ok=True)

            output_file = os.path.join(account_folder, "memo.json")

            with open(output_file, "w") as f:
                json.dump(memo, f, indent=4)

            print("Memo created for:", account_id)


if __name__ == "__main__":
    process_demo_calls()