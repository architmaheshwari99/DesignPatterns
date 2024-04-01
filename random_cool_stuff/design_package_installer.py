"""
1. On what environment is the package being installed and if the installer is compatible with the underlying environment ( Linux, Windows, ARM / AMD etc.)
2. The package installer would also contain 4 scripts such as the pre installer/post-installer / pre - uninstall / post-uninstall scripts, each of the scripts would perform the task of setting up the environment before the package is being installed or clean-up the environment after the package has been uninstalled.
3. Basic sanity tests should also be part of the installer such as : Does the system has required memory / space ? Does the installer has correct access write (e.g Sudo access for Linux machine etc .)
4. The package installer should also take care of the dependencies for the underline program, if certain dependencies are not available then the installer must ensure that all the dependencies have been successfully installed before proceeding with installing the program.
5. If the program needs to create certain directory / setting up environment paths, then the installer should ask the host machine/user for the required destination. The scripts for all these actions should be part of the pre-install script.
6. Once the program has been installed, the installer needs to know if the package should be executed immediately or would it be executed at a later point in time.
7. The installer also needs to take care of the clean-up. All the dependencies needs to be removed along with the base folder etc. The machine should be in the state as it was before installing the package.

Ex: A → {B,C}
    B → {E}
    C → {D,E,F}
    D → {}
    F → {}
    G → {C}

LLD for
  1. dependency resolution (Course Schedule 2) -> determine the prerequisites of a particular course
  2. Detecting Cyclic Dependency (Cycle Detection in a Cyclic Graph) -> We would need to maintain 2 sets to
                                        store visited and seen packages.

Algorithm: Topological Sort
"""


class Package:
    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def set_dependencies(self, *args):
        self.dependencies.extend(args)

    def get_dependencies(self):
        return self.dependencies

    def __str__(self):
        return self.name


class Order:
    def __init__(self) -> None:
        pass

    def get_build_order(self, package: Package):
        """returns the build order
        """
        order = []
        visited, seen = set(), set()

        def helper(cur_package):
            if cur_package in visited:
                return False

            if cur_package in seen:
                return True

            # {A, }
            # {E, B, }
            visited.add(cur_package)
            for package in cur_package.get_dependencies():
                if not helper(package):
                    return False

            visited.remove(cur_package)

            # Adding cur_package in seen to skip traversal on a package which is considered already, we can skip this
            # cur_package in seen implies it will exist in order(result array)
            seen.add(cur_package)
            order.append(cur_package)
            return True

        helper(package)
        return order


if __name__ == "__main__":
    A = Package('A')
    B = Package('B')
    C = Package('C')
    D = Package('D')
    E = Package('E')
    F = Package('F')
    G = Package('G')

    A.set_dependencies(B, C)
    B.set_dependencies(E)
    C.set_dependencies(D, E, F)
    G.set_dependencies(C)

    order_1 = Order()
    res = order_1.get_build_order(A)
    print(res)
