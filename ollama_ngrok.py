# Get Ngrok authentication token from colab secrets environment

import asyncio
import os

from google.colab import userdata

NGROK_AUTH_TOKEN = userdata.get('NGROK_AUTH_TOKEN')

# Set LD_LIBRARY_PATH so the system NVIDIA library becomes preferred
# over the built-in library. This is particularly important for
# Google Colab which installs older drivers
os.environ.update({'LD_LIBRARY_PATH': '/usr/lib64-nvidia'})

# Define run - a helper function to run subcommands asynchronously.
# The function takes in 2 arguments:
#  1. command
#  2. environment variable
async def run(cmd):
  print('>>> starting', *cmd)
  p = await asyncio.subprocess.create_subprocess_exec(
      *cmd,
      stdout=asyncio.subprocess.PIPE,
      stderr=asyncio.subprocess.PIPE
  )

  
# This function is designed to handle large amounts of text data efficiently.
# It asynchronously iterate over lines and print them, stripping and decoding as needed.
  async def pipe(lines):
    async for line in lines:
      print(line.strip().decode('utf-8'))


# Gather the standard output (stdout) and standard error output (stderr) streams of a subprocess and pipe them through
# the `pipe()` function to print each line after stripping whitespace and decoding UTF-8.
# This allows us to capture and process both the standard output and error messages from the subprocess concurrently.
  await asyncio.gather(
      pipe(p.stdout),
      pipe(p.stderr),
  )


# Authenticate with Ngrok
await asyncio.gather(
  run(['ngrok', 'config', 'add-authtoken', NGROK_AUTH_TOKEN])
)
