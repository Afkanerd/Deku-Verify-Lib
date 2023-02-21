<img src="https://github.com/Afkanerd/Afkanerd-Resources/raw/main/images/Artboard%209.png" align="right" width="350px"/>

# Deku Verify Plugin

Afkanerd Deku verification plugin

## Installation

Please make sure you have Python 3.7 or newer (python --version).

### Create a Virtual Environments

```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

### PyPI

```bash
$ pip install --upgrade pip wheel
$ pip install "git+https://github.com/Afkanerd/Deku-Verify-Plugin.git@main#egg=DekuVerify"
```

Install upgrades

```bash
$ pip install --force-reinstall "git+https://github.com/Afkanerd/Deku-Verify-Plugin.git@main#egg=DekuVerify"
```

### From source

```bash
$ git clone https://github.com/Afkanerd/Deku-Verify-Plugin.git
$ cd Deku-Verify-Plugin
$ python3 setup.py install
```

## Usage

### Table of Content

---

1. [Create Method](#create)
2. [Check Method](#check)
3. [Cancel Method](#cancel)

---

### Create

```python
from DekuVerify import Verification, MySQL

try:
    db_config = MySQL(
        database="",
        user="",
        host="",
        password="",
    )

    verify = Verification(database_params=db_config)

    result = verify.create(identifier)

except Exception as error:
    # Handle exception here ...

```

response

```json
{ "code": "", "sid": "", "identifier": "", "expires": "" }
```

### Check

```python
from DekuVerify import Verification, MySQL

try:
    db_config = MySQL(
        database="",
        user="",
        host="",
        password="",
    )

    verify = Verification(database_params=db_config)

    result = verify.check(sid, code, identifier)

except Exception as error:
    # Handle exception here ...

```

response

```json
{ "status": "", "sid": "", "identifier": "" }
```

### Cancel

```python
from DekuVerify import Verification, MySQL

try:
    db_config = MySQL(
        database="",
        user="",
        host="",
        password="",
    )

    verify = Verification(database_params=db_config)

    result = verify.cancel(sid)

except Exception as error:
    # Handle exception here ...

```

response

```json
bool
```

## Exceptions

- **SessionNotFound**: Exception raised when a verification session is not
  found.

  _return:_ String

- **IncorrectCode**: Exception raised when a given verification code is
  incorrect

  _return:_ String

- **InvalidIdentifier**: Exception raised when a given identifier is incorrect
  the mapped session

  _return:_ String

## Licensing

This project is licensed under the [GNU General Public License v3.0](LICENSE).
