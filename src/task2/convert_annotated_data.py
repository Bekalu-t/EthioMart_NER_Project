import re

def parse_annotated_file(file_path):
    TRAIN_DATA = []
    with open(file_path, 'r', encoding='utf-8') as f:
        text = ""
        entities = []
        for line in f:
            line = line.strip()
            if not line:  # Skip empty lines
                if text and entities:
                    TRAIN_DATA.append((text.strip(), {"entities": entities}))
                    text = ""
                    entities = []
                continue
            # Find all tagged entities
            for match in re.finditer(r'\[(.*?)\](.*?)\[/\1\]', line):
                label = match.group(1)
                entity_text = match.group(2)
                start = text.index(f'[{label}]{entity_text}[/{label}]') if f'[{label}]{entity_text}[/{label}]' in text else len(text)
                end = start + len(entity_text)
                entities.append((start, end, label))
                # Remove tags from text
                line = line.replace(f'[{label}]{entity_text}[/{label}]', entity_text)
            text += line + " "
        if text and entities:
            TRAIN_DATA.append((text.strip(), {"entities": entities}))
    return TRAIN_DATA

# Save to file for use in train_ner_model.py
annotated_file = 'src/task2/annotated_ner_sample.txt'
train_data = parse_annotated_file(annotated_file)
with open('src/task2/train_data.py', 'w', encoding='utf-8') as f:
    f.write('TRAIN_DATA = ' + str(train_data))
print("TRAIN_DATA saved to src/task2/train_data.py")