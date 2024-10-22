# atuin-rpmspec

Tools to build and package [Atuin](https://atuin.sh/) for RPM-based distros.

## Instructions

You must have user.name and user.email set in your `~/.gitconfig` for rust2rpm to work, so:

```sh
git config --global user.name 'Firstname Lastname'
git config --global user.email 'my@emailaddress.com'
```

...if you haven't already.


Clone the repo then:

```sh
# build and install
make tools      # install the required packages
make spec       # generate the RPM spec file
make rpm        # compile atuin and build the RPM
make install    # install the RPM/package

# the following are also provided
make uninstall  # uninstall the package
make clean      # remove crates and vendor files
```

Please see the `Makefile` for details on what each target does.
