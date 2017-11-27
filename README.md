# Rclone Mount

This is a script to mount and unmount remotes defined in a json file for rclone.
A config file must be made.

## Example Config

```
[{
    "source": "gsuite:/videos/",
    "dest": "~/Videos/Gsuite",
    "read_only": true
},
{
    "source": "onedrive:/Videos",
    "dest": "~/Videos/Onedrive",
    "read_only": true
},
{
    "source": "onedrive:/private_folder",
    "dest": "~/Private",
    "umask": "077",
    "read_only": true
}]
```

A umask may be used to set permissions on files within a mount point.