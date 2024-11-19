from thku_rss.main import main
import argparse
import texteditor
import pkg_resources

config_file = pkg_resources.resource_filename("thku_rss", "config.json")

def launch():
    parser = argparse.ArgumentParser(prog="thku_rss", description="THK Üniversitesi Duyuruları RSS Kaynağı Oluşturucu")
    parser.add_argument("-c", "--config", help="Configure XML file locations, databases etc.", action="store_true")
    parser.add_argument("-f", "--fetch", help="Fetch items", action="store_true")
    args = parser.parse_args()

    if args.config:
        texteditor.open(filename=config_file)
    elif args.fetch:
        main()
        exit()
