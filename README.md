# Rclone Mount

This is a script to mount and unmount remotes defined in a json file for rclone.
A config file must be made.
## Example Config

```
[{
    "source": "gsuite:/videos/",
    "dest": "~/Videos/Gsuite"
},
{
    "source": "onedrive:/Videos",
    "dest": "~/Videos/Onedrive"
}]
```