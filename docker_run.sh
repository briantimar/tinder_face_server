#/bin/bash
docker run -v$(pwd):/tmp -w /tmp bamos/openface python $(pwd)/generate_labeled_pictures.py