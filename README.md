# PyWebOSTVWrapper

## Installation

```python
$ pip install pywebostv
```

### macOS Big Sur

If you see errors such as opensslv.h file not found, it most likely indicates that you don't have a working installation of OpenSSL. In such a case, we would recommend that you install it using the following steps (assuming you've brew as your package manager):

```python
$ brew install openssl
$ env LDFLAGS="-L$(brew --prefix openssl)/lib" CFLAGS="-I$(brew --prefix openssl)/include" pip3 install cryptography
$ pip3 install pywebostv
```


## How to Use: Connecting to the TV

### Establishing the connection.

```python
from pywebostv.discovery import *    # Because I'm lazy, don't do this.
from pywebostv.connection import *
from pywebostv.controls import *

tv = TVControl("IP")
tv.MediaControls("volume_up") # for up volume

```

**NOTE**: If you're seeing repeated prompts on the TV to re-authenticate, there's a good chance you're not using the `store` correctly. Read the FAQs section for more.

### API Details

Please note that all the examples below use the blocking calls. Their return values and structure
are documented in the comments. They throw python exceptions when unsuccessful. To make non-blocking
calls, refer to the section above.

### Media Controls

```python
tv = TVControl("IP")

tv.MediaControls("volume_up")
tv.MediaControls("volume_down")
tv.MediaControls("get_volume")
tv.MediaControls("set_volume")
tv.MediaControls("mute")
tv.MediaControls("pause")
tv.MediaControls("rewind")
tv.MediaControls("fast_forward")

tv.MediaControls("get_audio_output")
audio_outputs = tv.MediaControls("list_audio_output_sources")
tv.MediaControls("set_audio_output", audio_outputs[0])
```

the library it's for easy use webostv API
