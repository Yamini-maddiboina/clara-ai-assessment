import os
import json

DATASET_DIR = "dataset"
OUTPUT_DIR = "output"


def process_onboarding():

    for file in os.listdir(DATASET_DIR):

        if file.startswith("onboarding_call_") and file.endswith(".txt"):

            account_id = file.replace("onboarding_call_", "").replace(".txt", "")

            transcript_path = os.path.join(DATASET_DIR, file)

            with open(transcript_path, "r", encoding="utf-8") as f:
                transcript = f.read().lower()

            v1_path = os.path.join(OUTPUT_DIR, account_id, "v1", "memo.json")

            if not os.path.exists(v1_path):
                continue

            with open(v1_path) as f:
                memo = json.load(f)

            changes = {}

            if "24/7" in transcript:
                memo["business_hours"]["days"] = "all days"
                changes["business_hours"] = "Updated to 24/7"

            if "new address" in transcript:
                memo["office_address"] = "Updated during onboarding"
                changes["office_address"] = "Address updated"

            v2_folder = os.path.join(OUTPUT_DIR, account_id, "v2")
            os.makedirs(v2_folder, exist_ok=True)

            memo_path = os.path.join(v2_folder, "memo.json")

            with open(memo_path, "w") as f:
                json.dump(memo, f, indent=4)

            changelog = {
                "account_id": account_id,
                "version_from": "v1",
                "version_to": "v2",
                "changes": changes
            }

            change_file = os.path.join(v2_folder, "changes.json")

            with open(change_file, "w") as f:
                json.dump(changelog, f, indent=4)

            print("Account updated:", account_id)


if __name__ == "__main__":
    process_onboarding()