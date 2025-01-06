import json
import pandas as pd

DEFAULT_SYSTEM_PROMPT = 'Eres un intérprete de Lengua de Señas de Guatemala. El usuario te va a dar frases escritas en español que utilizan la gramática de Lengua de Señas de Guatemala. Tu trabajo es interpretar estas frases y escribirlas en español con la gramática correcta.'

# ----------------- Create dataset ----------------- #
# Function: create_dataset
# Description: Creates a dataset in the format required by the model
# Parameters:
#       - question: question to ask user
#       - answer: answer to question
# Return:
#       - dataset: dataset in the required format
# ----------------------------------------------- #
def create_dataset(question, answer):
    return {
        "messages": [
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": question + " ->"},
            {"role": "assistant", "content": answer},
        ]
    }

# ----------------- Main ----------------- #
# Description: Reads data from a csv file and creates a jsonl file with the data in the required format
# Parameters: None
# Return: None
# -------------------------------------- #
def main():
    file_train = "./SenasChapinas_ProcesamientoDeLenguajeNatural/src/dataset/processed/train_data.csv"              # File with training data
    file_validation = "./SenasChapinas_ProcesamientoDeLenguajeNatural/src/dataset/processed/validation_data.csv"    # File with validation data

    train_df = pd.read_csv(file_train, encoding="utf-8")                            # Read training data
    validation_df = pd.read_csv(file_validation, encoding="utf-8")                  # Read validation data

    train_df = train_df.rename(columns={"LENSEGUA": "Question", "ESPAÑOL": "Answer"})           # Rename columns
    validation_df = validation_df.rename(columns={"LENSEGUA": "Question", "ESPAÑOL": "Answer"}) # Rename columns

    with open("./SenasChapinas_ProcesamientoDeLenguajeNatural/src/dataset/processed/train.jsonl", "w", encoding="utf-8") as f:
        for _, row in train_df.iterrows():
            example_str = json.dumps(create_dataset(row["Question"], row["Answer"]), ensure_ascii=False)
            f.write(example_str + "\n")

    with open("./SenasChapinas_ProcesamientoDeLenguajeNatural/src/dataset/processed/validation.jsonl", "w", encoding="utf-8") as f:
        for _, row in validation_df.iterrows():
            example_str = json.dumps(create_dataset(row["Question"], row["Answer"]), ensure_ascii=False)
            f.write(example_str + "\n")

if __name__ == '__main__':
    main()