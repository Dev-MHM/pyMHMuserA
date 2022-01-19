# Installation
```bash
pip3 install -U py-MHMUser
```


# Usage
- Create folders named `plugins`, `addons`, `assistant` and `resources`.   
- Add your plugins in the `plugins` folder and others accordingly.   
- Create a `.env` file with following mandatory Environment Variables
   ```
   API_ID
   API_HASH
   SESSION
   REDIS_URI
   REDIS_PASSWORD
   ```


## Creating plugins
 - ### To work everywhere

```python
@mhmuser_cmd(
    pattern="start"
)   
async def _(e):   
    await e.eor("MHMuser Started!")   
```

- ### To work only in groups

```python
@mhmuser_cmd(
    pattern="start",
    groups_only=True,
)   
async def _(e):   
    await eor(e, "MHMuser Started.")   
```

- ### Assistant Plugins 👇

```python
@asst_cmd("start")   
async def _(e):   
    await e.reply("MHMuser Started.")   
```

See more working plugins on [the offical repository](https://github.com/Dev-MHM/pyMHMuser)!

> Made with 💕 by [@MHMuser](https://t.me/MHMuser).    



