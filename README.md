# Argeye - a small improved version of Argparse

`argeye` retains all the original usage of `argparse`,but adding a yml file so user can modify arguments by editing yml file.

> argparse supports command lines to set arguments,whose disadvantages is that the user have to type the arg strings and values.
>
> the typing is a redundant operation,which may cause mistakes and counterintuitive understanding of the args.
>
> yml file provides intuitive understanding and a more convenient way to set args.

## usage

### (original)

retained all the original usage of argparse,detailed info refer to [official document](https://docs.python.org/3/library/argparse.html)

### (new)

#### first run (same as running argparse)

```python
# examples/main.py
from argeye import ArgumentParser

parser = ArgumentParser()
parser.add_argument("equip_name", type=str, default="wired")
parser.add_argument("--model_name", default="pd", type=str)
parser.add_argument("--finetune", default=False, type=bool)

args = parser.parse_args()
print(args)
```

```python
# decide whether to input arguments at the terminal based on actual needs
$ python examples/main.py
Namespace(equip_name='wired',model_name='pd',finetune=True)
```

after executing the above command line operations,the yml file will be created in the work directory.

the content of the yml file is as follows:

```yml
equip_name: wired
--model_name: pd
--finetune: false
```

now having the yml file,the user can change arguments values by editing yml file instead of typing strings into command lines.

when the change operation is completed(completed in the yml file),simply run the python file without the need of typing arguments on the command line.

**example:**

```yml
# change arguments in the yml file
equip_name: wireless
--model_name: resnet
--finetune: True
```

```python
# run python file directly
$ python examples/main.py
Namespace(equip_name='wireless', model_name='resnet', finetune=True)
```

## installation

`pip install argeye`
