import argparse
import transcribeUtils
import srtUtils
import boto3

# Get the command line arguments and parse them
parser = argparse.ArgumentParser( prog='srt.py', description='Transfer aws transcript.json to .srt subtitle file.')
parser.add_argument('-tsKey', required=True, help='transcription json file subtitle file')
parser.add_argument('-srtFile', required=True, help='.srt subtitle file')
args = parser.parse_args()


s3 = boto3.client('s3')
response = s3.get_object(Bucket='cp4cc-test', Key=args.tsKey)
ts = response['Body'].read()
srtUtils.writeTranscriptToSRT(ts, "EN", args.srtFile)
