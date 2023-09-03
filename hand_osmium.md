```bash
docker run -w /wkd -v /home/arodionov/pbfs:/wkd mschilde/osmium-tool osmium add-locations-to-ways planet-230313.osm.pbf -v --output-format pbf,pbf_compression=none --keep-untagged-nodes -i flex_mem -o  planet_loc_ways.pbf;
```


```bash
docker run -w /wkd -v /home/arodionov/pbfs:/wkd mschilde/osmium-tool osmium export  -e --config=/home/arodionov/pbfs/planet-230313_loc_ways/static/osmium_export.json --fsync -i flex_mem --geometry-types polygon  -v -f pg -x tags_type=hstore /home/arodionov/pbfs/planet-230313.osm.pbf -o /home/arodionov/pbfs/planet-230313_loc_ways/multipolygon/source.tsv;
```
