import numpy as np

def set_border_values(image, value):
    """Set edge values along all axes to a constant value.

    Parameters
    ----------
    image : ndarray
        The array to modify inplace.
    value : scalar
        The value to use. Should be compatible with `image`'s dtype.

    Examples
    --------
    >>> image = np.zeros((4, 5), dtype=int)
    >>> _set_border_values(image, 1)
    >>> image
    array([[1, 1, 1, 1, 1],
           [1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1],
           [1, 1, 1, 1, 1]])
    """
    for axis in range(image.ndim):
        # Index first and last element in each dimension
        sl = (slice(None),) * axis + ((0, -1),) + (...,)
        image[sl] = value
        
def fast_pad(image, value, *, order="C"):
    """Pad an array on all axes by one with a value.

    Parameters
    ----------
    image : ndarray
        Image to pad.
    value : scalar
         The value to use. Should be compatible with `image`'s dtype.
    order : "C" or "F"
        Specify the memory layout of the padded image (C or Fortran style).

    Returns
    -------
    padded_image : ndarray
        The new image.

    Notes
    -----
    The output of this function is equivalent to::

        np.pad(image, 1, mode="constant", constant_values=value)

    Up to versions < 1.17 `numpy.pad` uses concatenation to create padded
    arrays while this method needs to only allocate and copy once.
    This can result in significant speed gains if `image` has a large number of
    dimensions.
    Thus this function may be safely removed once that version is the minimum
    required by scikit-image.

    Examples
    --------
    >>> _fast_pad(np.zeros((2, 3), dtype=int), 4)
    array([[4, 4, 4, 4, 4],
           [4, 0, 0, 0, 4],
           [4, 0, 0, 0, 4],
           [4, 4, 4, 4, 4]])
    """
    # Allocate padded image
    new_shape = np.array(image.shape) + 2
    new_image = np.empty(new_shape, dtype=image.dtype, order=order)

    # Copy old image into new space
    sl = (slice(1, -1),) * image.ndim
    new_image[sl] = image
    # and set the edge values
    set_border_values(new_image, value)

    return new_image