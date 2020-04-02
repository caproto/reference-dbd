# reference-dbd
Reference IOC database definition + related information for generating the
caproto.server.records module

## Source of database definitions
`motorSim.dbd` sourced from v0.2 of
https://hub.docker.com/r/hhslepicka/epics-devel

## To rebuild

```bash
$ make clean records.py
```

To copy to the caproto source tree:
```bash
$ CAPROTO=/path/to/caproto make copy
```
