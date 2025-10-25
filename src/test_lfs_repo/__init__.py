def main() -> None:
    print("Hello from test-lfs-repo!")

def main_lfs() -> None:
    from .lfs_module import LFS_TEST
    from .another_lfs_module import ANOTHER_LFS_TEST
    print(f"Hello from test-lfs-repo! {LFS_TEST=} {ANOTHER_LFS_TEST=}")
