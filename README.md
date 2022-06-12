# Introduction à Python

## Cours accesibles :
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) 1.1 - Les Variables.ipynb](https://colab.research.google.com/github/paul-leydier/py-intro/blob/main/notebooks/1.1%20-%20Les%20Variables.ipynb)
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) 1.2 - Les Controles logiques.ipynb](https://colab.research.google.com/github/paul-leydier/py-intro/blob/main/notebooks/1.2%20-%20Les%20controles%20logiques.ipynb)
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) 1.3 - Les listes.ipynb](https://colab.research.google.com/github/paul-leydier/py-intro/blob/main/notebooks/1.3%20-%20Les%20listes.ipynb)
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) 1.4 - Les dictionnaires.ipynb](https://colab.research.google.com/github/paul-leydier/py-intro/blob/main/notebooks/1.4%20-%20Les%20dictionnaires.ipynb)
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) 1.5 - Les boucles.ipynb](https://colab.research.google.com/github/paul-leydier/py-intro/blob/main/notebooks/1.5%20-%20Les%20boucles.ipynb)
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) 1.6 - Les fonctions.ipynb](https://colab.research.google.com/github/paul-leydier/py-intro/blob/main/notebooks/1.6%20-%20Les%20fonctions.ipynb)
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) 1.7 - Exercice de synthese.ipynb](https://colab.research.google.com/github/paul-leydier/py-intro/blob/main/notebooks/1.7%20-%20Exercice%20de%20synthese.ipynb)

---

# Contribution

### Clean a notebook before commit

```commandline
jupyter nbconvert --clear-output --inplace ./notebooks/*.ipynb
```

### Hide some code within a cell (For example, to hide the solution to an exercise)
- Add the following snippet at the beginning of the cell
```markdown
#@title Cliquez ici pour la solution.
```
- Add the following tag to the cell's metadata: `"cellView": "form"`
