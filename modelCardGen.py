import fire
import os

def parseMetadata(contents):
    metadata = {}
    lines = contents.split('\n')
    in_metadata = False
    for line in lines:
        if line.strip() == '---':
            if in_metadata:
                break
            else:
                in_metadata = True
                continue
        if in_metadata and ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()
    return metadata

model_id = os.getenv('MODEL_ID')
model_creator, model_name = model_id.split('/')

def modelCardGen():
    # Read README.md
    with open(f'./${{ env.MODEL_NAME }}/README.md', 'r') as file:
        contents = file.read()

    # Parse existing metadata
    metadata = parse_metadata(contents)

    # Update metadata
    metadata['base_model'] = metadata.get('base_model', model_id)
    metadata['model_creator'] = metadata.get('model_creator', model_creator)
    metadata['model_name'] = metadata.get('model_name', model_name)
    metadata['quantized_by'] = metadata.get('quantized_by', 'Jan')
    metadata['language'] = metadata.get('language', '- en')
    metadata['pipeline_tag'] = metadata.get('pipeline_tag', 'conversational')

    # Reconstruct README
    updated_readme = '---\n' + '\n'.join(f'{k}: {v}' for k, v in metadata.items()) + '\n---\n' + contents.split('---\n', 2)[-1]

    # Write updated README.md
    with open(f'./${{ env.MODEL_NAME }}/README.md', 'w') as file:
        file.write(updated_readme)

if __name__ == '__main__':
    fire.Fire(parse_metadata)