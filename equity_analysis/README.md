1) download file https://www.quandl.com/api/v3/databases/SF1/data?auth_token=nmpd4FBBYEyUZj3wn91k



2) unzip

3) separate ticker

sed -i '' -e 's/_/,/' <filename>

4) put separator for rows with no period

sed -i '' -e 's/,200[3-9]-/,&/' <filename>

sed -i '' -e 's/,201[1-9]-/,&/‘ <filename>



5) extract period ARQ, ARY, etc.

sed -i '' -e 's/_ARQ,/&ARQ/'  <filename>

sed -i '' -e 's/_ARY,/&ARY/' <filename>

sed -i '' -e 's/_ART,/&ART/' <filename>

sed -i '' -e 's/_MRQ,/&MRQ/' <filename>

sed -i '' -e 's/_MRT,/&MRT/' <filename>

sed -i '' -e 's/_MRY,/&MRY/' <filename>