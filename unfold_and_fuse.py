import argparse
import glob
from pathlib import Path

import cv2 as cv
import numpy as np


def unfold_and_fuse(files, indices, tol, gap, edge, sample_radius, reverse=False):
    left = edge - gap - tol
    right = edge
    if reverse:
        indices.reverse()
    for i, indx in enumerate(indices):
        fl = files[0].replace("00001", str(indx).zfill(5))
        img = cv.imread(fl)
        center = (img.shape[1] / 2, img.shape[2] / 2)
        img2 = cv.logPolar(img, center, sample_radius, cv.WARP_FILL_OUTLIERS)
        if i == 0:
            base_img = img2.copy()
        else:
            section = img2[:, left:right].copy()
            cv.imwrite(fl.replace("frame", "Test"), section)
            base_img = np.append(base_img, base_img[:, :gap], axis=1)
            base_img[:, (left + i * gap) : (right + i * gap)] = section[:, :]

    return base_img


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", type=int, help="Start frame.")
    parser.add_argument("-e", "--end", type=int, help="End frame.")
    parser.add_argument("-g", "--gap", type=int, help="Gap between unfolded frames.")
    parser.add_argument(
        "-r", "--sample_radius", type=float, help="Samle Radius of cv.logPolar"
    )
    parser.add_argument(
        "-t", "--tolerance", type=int, help="Width, in pixels, to sample"
    )
    parser.add_argument(
        "-d", "--edge", type=int, help="The right-most pixel to sample."
    )

    parser.add_argument("in_dir", type=str, help="The directory of frames_*.png.")

    args = parser.parse_args()
    # start = 1044
    # end = 1486
    # step = 7
    # edge = 539
    # tol = 20
    # sample_radius = 94.5
    in_dir = Path(args.in_dir)
    files = glob.glob(in_dir / "frame_*.png")
    files.sort()
    indices = range(args.start, args.end + 1)

    result = unfold_and_fuse(
        files,
        indices,
        args.tolerance,
        args.gap,
        args.edge,
        args.sample_radius,
        reverse=False,
    )

    cv.imwrite(in_dir / "Result.png", result)
