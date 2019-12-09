# Alice Skill Kit

The Alice Skill Kit is a tool that helps creating Skills for Alice.

## Features
- [create a new Skill](https://github.com/project-alice-powered-by-snips/ProjectAliceSkillKit/blob/master/CreateSkills.md)
- [validate the format of all json files](https://github.com/project-alice-powered-by-snips/ProjectAliceSkillKit/blob/master/Validation.md)

## Install
```bash
pip3 install alice-sk
```
The Skill Kit supports tab completion for `bash` and `zsh` it can be activated by adding this in your .bashrc:
```bash
eval "$(_ALICE_SK_COMPLETE=source alice-sk)"
```
For zsh users add this to your .zshrc:
```bash
eval "$(_ALICE_SK_COMPLETE=source_zsh alice-sk)"
```

## Testing
It is possible to run all validation tests we currently run against a skill when someone submits a PR locally using:
```bash
alice-sk validate --path <pathnames>
```
Further information on the validation tests can be found [here](https://github.com/project-alice-powered-by-snips/ProjectAliceSkillKit/blob/master/Validation.md)


## Auto skills creation
TO create the basic files needed for a skill to work run:
```bash
alice-sk create
```
This saves you the hassle of creating the directory tree, the required files and so on. It also follows the strict conventions we made for skills and will avoid you trouble when submitting your skill for review.
