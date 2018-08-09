import urllib.request
import gzip
import shutil

# Download metadata
urllib.request.urlretrieve("http://ftp.us.debian.org/debian/dists/testing/main/binary-amd64/Packages.gz", 
"main.gz")
urllib.request.urlretrieve("http://ftp.us.debian.org/debian/dists/testing/contrib/binary-amd64/Packages.gz", 
"contrib.gz")
urllib.request.urlretrieve("http://ftp.us.debian.org/debian/dists/testing/non-free/binary-amd64/Packages.gz", 
"nonfree.gz")
print("Downloading metadata completed.")

# Extract metadata
with gzip.open('main.gz', 'rb') as f_in:
    with open('main', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
with gzip.open('contrib.gz', 'rb') as f_in:
    with open('contrib', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
with gzip.open('nonfree.gz', 'rb') as f_in:
    with open('nonfree', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
print("Extracting metadata completed.")

# Parse metadata
with open("main", encoding='utf-8') as fin:
    with open("mainList.txt", "w", encoding="utf-8") as fout:
        for line in fin:
            if line.startswith("Package: "):
                packageName = line[9:]
                fout.write(packageName)
with open("contrib", encoding='utf-8') as fin:
    with open("contribList.txt", "w", encoding="utf-8") as fout:
        for line in fin:
            if line.startswith("Package: "):
                packageName = line[9:]
                fout.write(packageName)
with open("nonfree", encoding='utf-8') as fin:
    with open("nonfreeList.txt", "w", encoding="utf-8") as fout:
        for line in fin:
            if line.startswith("Package: "):
                packageName = line[9:]
                fout.write(packageName)
print("Parsing metadata completed.")

# Merge files
filenames = ['mainList.txt', 'contribList.txt', 'nonfreeList.txt']
with open('debianAllPackagesList.txt', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			for line in infile:
				outfile.write(line)
print("Debian metadata is ready.")
