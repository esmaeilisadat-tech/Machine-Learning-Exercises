import os
from pathlib import Path

workspace_dir = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace')
repo_base_url = "esmaeilisadat-tech/Machine-Learning-Exercises/blob/main"
raw_base_url = "esmaeilisadat-tech/Machine-Learning-Exercises/raw/main"

projects = [
    '01-ml-engineering-foundations',
    '02-advanced-data-preprocessing',
    '03-imbalanced-learning-techniques',
    'anomaly-detection-outlier-analysis',
    'autoencoder-feature-extraction',
    'automl-pipeline-optimization',
    'computer-vision-cnn-cats-dogs',
    'customer-segmentation-rfm-kmeans',
    'decision-trees-predictive-modeling',
    'dimensionality-reduction-pca-wine',
    'ensemble-learning-model-comparison',
    'gradient-boosting-performance-tuning',
    'hyperparameter-optimization-machine-learning',
    'reinforcement-learning-cartpole'
]

def format_project_name(name):
    # E.g. '01-ml-engineering-foundations' -> 'ML Engineering Foundations'
    parts = name.split('-')
    if parts[0].isdigit():
        parts = parts[1:]
    return ' '.join(p.capitalize() for p in parts)

for proj in projects:
    proj_dir = workspace_dir / proj
    if not proj_dir.exists(): continue
    
    title = format_project_name(proj)
    
    readme_content = f"# {title}\n\n"
    readme_content += "This project is part of my Machine Learning Engineering Portfolio.\n\n"
    
    # Notebooks section
    readme_content += "## Interactive Notebooks\n\n"
    readme_content += "You can view or run these notebooks interactively using the links below:\n\n"
    
    notebooks_dir = proj_dir / 'notebooks'
    if notebooks_dir.exists():
        nbs = [nb.name for nb in notebooks_dir.glob('*.ipynb') if '.ipynb_checkpoints' not in str(nb)]
        # Sort so Anfaenger, Fortgeschrittene, Experte are roughly in order
        order = {'Anfaenger.ipynb': 1, 'Fortgeschrittene.ipynb': 2, 'Experte.ipynb': 3}
        nbs.sort(key=lambda x: order.get(x, 99))
        
        for nb in nbs:
            colab_link = f"https://colab.research.google.com/github/{repo_base_url}/{proj}/notebooks/{nb}"
            nbviewer_link = f"https://nbviewer.jupyter.org/github/{repo_base_url}/{proj}/notebooks/{nb}"
            github_link = f"https://github.com/{repo_base_url}/{proj}/notebooks/{nb}"
            
            readme_content += f"### {nb.replace('.ipynb', '')}\n"
            readme_content += f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_link}) "
            readme_content += f"[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)]({nbviewer_link}) "
            readme_content += f"[![View on GitHub](https://img.shields.io/badge/View-on%20GitHub-blue?logo=github)]({github_link})\n\n"
    
    # Datasets section
    readme_content += "## Datasets\n\n"
    data_dir = proj_dir / 'data'
    if data_dir.exists():
        data_files = [f.name for f in data_dir.glob('*') if f.is_file() and f.name != '.gitkeep' and f.name != 'README.md']
        if data_files:
            readme_content += "The following datasets are used in this project:\n\n"
            for df in data_files:
                gh_link = f"https://github.com/{repo_base_url}/{proj}/data/{df}"
                raw_link = f"https://raw.githubusercontent.com/{raw_base_url}/{proj}/data/{df}"
                readme_content += f"- **{df}**: [View in Repo]({gh_link}) | [Download Raw]({raw_link})\n"
        else:
            readme_content += "This project uses internally generated data or datasets fetched via APIs within the code.\n\n"
    else:
        readme_content += "This project uses internally generated data or datasets fetched via APIs within the code.\n\n"

    # Outputs section
    readme_content += "\n## Outputs & Results\n\n"
    readme_content += "Generated visualizations and metrics are stored in the output/ directory (categorized by difficulty level).\n\n"
    readme_content += "---\n*Generated automatically for the ML Engineering Portfolio*\n"
    
    readme_path = proj_dir / 'README.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"Generated README for {proj}")

print("All READMEs generated successfully!")
