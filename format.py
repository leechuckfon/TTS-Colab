import os
import argparse

from trainer import Trainer, TrainerArgs
from TTS.demos.xtts_ft_demo.utils.formatter import format_audio_list
from TTS.demos.xtts_ft_demo.utils.formatter import list_audios



def main():
  parser = argparse.ArgumentParser(
        description="""XTTS fine-tuning demo\n\n"""
        """
        Example runs:
        python3 TTS/demos/xtts_ft_demo/xtts_demo.py --port 
        """,
        formatter_class=argparse.RawTextHelpFormatter,
  )
  parser.add_argument(
        "--path",
        type=str,
        help="Port to run the gradio demo. Default: 5003",
        default="/content/xtts",
  )

  args = parser.parse_args();

  format_audio_list(args.path)

if __name__ == "__main__":
    main()
