"""
main runner
"""

from instagram_coll import InstagramColl


def main():
    """
    go find some data and bring it back.
    :return:
    """
    insta_test = InstagramColl(33, 12, 5000)
    insta_test.start()

if __name__ == "__main__":
    main()
