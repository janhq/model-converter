import os
import yaml
import fire

def modify_metadata(model_id):
    """
    Modify the metadata of the README.md based on the model_id.
    Args:
    model_id (str): The model identifier in the format 'creator/name'.
    Returns:
    str: Updated YAML metadata as a string.
    """
    model_creator, model_name = model_id.split('/')

    # Read the original README.md content
    with open(f'./${{ env.MODEL_NAME }}/README.md', 'r') as file:
        content = file.read()

    # Extract the YAML part from the content
    yaml_part = content.split('---')[1]

    # Parse the YAML content
    data = yaml.safe_load(yaml_part)

    # Update the YAML data with dynamic values
    data['base_model'] = model_id
    data['model_creator'] = model_creator
    data['model_name'] = model_name
    data['quantized_by'] = 'Jan'

    # Convert the updated data back to YAML
    return yaml.safe_dump(data, sort_keys=False)

def additional_content(model_id):
    model_creator, model_name = model_id.split('/')
    static_text =f"""
<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/janhq/jan/assets/89722390/35daac7d-b895-487c-a6ac-6663daaad78e" alt="Jan banner" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>

<p align="center">
    <a href="https://jan.ai/">Jan</a> 
    - <a href="https://discord.gg/AsJ8krTT3N">Discord</a>
</p>
<!-- header end -->

# Model Description
This is a GGUF version of [{model_id}](https://huggingface.co/{model_id})
- Model creator: [{model_creator}](https://huggingface.co/{model_creator})
- Original model: [{model_name}](https://huggingface.co/{model_id})
- Model description: [Readme](https://huggingface.co/{model_id}/blob/main/README.md)

# About Jan
Jan believes in the need for an open-source AI ecosystem and is building the infra and tooling to allow open-source AIs to compete on a level playing field with proprietary ones.

Jan's long-term vision is to build a cognitive framework for future robots, who are practical, useful assistants for humans and businesses in everyday life.

# Jan Model Converter
This is a repository for the opensource converter. We are grateful if community can contribute and strengthen this repo. We are aiming to expand the repo that can convert into various type of format
"""
    return static_text

def update_readme():
    """
    Update the README.md file based on the environment variables.
    """
    model_id = os.getenv('MODEL_ID')
    if not model_id:
        raise ValueError("MODEL_ID environment variable is not set.")

    updated_yaml = modify_metadata(model_id)
    additional_md = additional_content(model_id)

    # Reconstruct the README content
    updated_content = '---\n' + updated_yaml + '---\n' + additional_md

    # Write the updated content back to README.md
    with open(f'./${{ env.MODEL_NAME }}/README.md', 'w') as file:
        file.write(updated_content)

if __name__ == '__main__':
    fire.Fire(update_readme)
