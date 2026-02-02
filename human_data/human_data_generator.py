import json
import os
from pathlib import Path
from datasets import load_dataset

# download and generate combined JSON file from the eli5_category dataset
def generate_json_files(output_dir="human_data/output"):
    
    script_dir = Path(__file__).parent
    os.makedirs(output_dir, exist_ok=True)

    dataset = load_dataset(str(script_dir / "eli5_category.py"), trust_remote_code=True)
    
    # Combine all splits into one dataset
    combined_data = []
    
    for split_name, split_data in dataset.items():
        print(f"Loading {split_name} split ({len(split_data)} examples)...")
        
        for example in split_data:
            combined_data.append(dict(example))
    
    # Save combined dataset to a single JSON file
    output_file = os.path.join(output_dir, f"eli5_combined.json")
    
    print(f"\nSaving combined dataset...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=2, ensure_ascii=False)
    
    file_size = os.path.getsize(output_file) / (1024 * 1024)
    print(f"\nCombined dataset: {len(combined_data)} examples, {file_size:.2f} MB")


if __name__ == "__main__":
    try:
        generate_json_files()
    except Exception as e:
        import traceback
        traceback.print_exc()
