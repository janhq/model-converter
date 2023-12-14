import os
import yaml
import fire

def modifyMetadata(modelId, modelAuthor, modelName):
    """
    Update the metadata of the model.
    """
    with open(f'./{modelName}/README.md', 'r') as file:
        content = file.read()

    yaml_part = content.split('---')[1]
    data = yaml.safe_load(yaml_part)

    data['base_model'] = modelId
    data['model_creator'] = modelAuthor
    data['model_name'] = modelName
    data['quantized_by'] = 'JanHQ'

    return yaml.safe_dump(data, sort_keys=False)

def modifyAdditionalMetadata(modelID, modelAuthor, modelName):
    
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
This is a GGUF version of [{modelID}](https://huggingface.co/{modelID})
- Model creator: [{modelAuthor}](https://huggingface.co/{modelAuthor})
- Original model: [{modelName}](https://huggingface.co/{modelID})
- Model description: [Readme](https://huggingface.co/{modelID}/blob/main/README.md)

# About Jan
Jan believes in the need for an open-source AI ecosystem and is building the infra and tooling to allow open-source AIs to compete on a level playing field with proprietary ones.

Jan's long-term vision is to build a cognitive framework for future robots, who are practical, useful assistants for humans and businesses in everyday life.

# Jan Model Converter
This is a repository for the [open-source converter](https://github.com/janhq/model-converter). We would be grateful if the community could contribute and strengthen this repository. We are aiming to expand the repo that can convert into various types of format
"""
    return static_text

def update_readme(modelId):
    """
    Update the README.md of the model folder.
    """
    if not modelId:
        raise ValueError("Please add ModelID.")

    modelAuthor, modelName = modelId.split('/')
    updated_yaml = modifyMetadata(modelId, modelAuthor, modelName)
    additional_md = modifyAdditionalMetadata(modelId, modelAuthor, modelName)

    updated_content = '---\n' + updated_yaml + '---\n' + additional_md
    modelName_lowercase = modelName.lower()
    with open(f'./{modelName_lowercase}/README.md', 'w') as file:
        file.write(updated_content)
    
    print('README.md updated successfully.')

if __name__ == '__main__':
    fire.Fire(update_readme)
