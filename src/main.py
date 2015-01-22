"""
main runner
"""

from instagram_coll import InstagramColl


def main():
    """
    go find some data and bring it back.
    :return:
    """
    insta_test = InstagramColl()
    insta_test.start()

if __name__ == "__main__":
    main()
