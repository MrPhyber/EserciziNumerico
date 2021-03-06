import matplotlib.pyplot as plt
from functools import reduce


PLOT_LABEL = 'label'
PLOT_POINTS = 'points'
PLOT_STYLE = 'style'


def make_simple_figure(points, title=None):
    """
    Get the points generated by evaluate_function() and return
    a matplotlib figure object.
    You can display the plot by calling .show() on it.

    >>> make_simple_figure(((1, 2), (2, 3), (3, 4))).show() # doctest: +SKIP
    """
    # ((1, 2), (3, 4), (5, 6))  ->  ((1, 3, 5), (2, 4, 6))
    xs, ys = tuple(zip(*points))

    x_range = (min(xs), max(xs))
    y_range = (min(ys), max(ys))

    figure, axes = plt.subplots()
    if title is not None:
        axes.set_title(title)
    axes.axis([*x_range, *y_range])
    axes.plot(xs, ys)
    return figure


def get_global_range(points_list):
    """
    Given a list of points (e.g. the xs and the ys returned
    by two different functions), return the minimum and the
    maximum value of the xs and the ys.

    >>> get_global_range(
    ...    (((1, 2), (-3, 4), (5, 6)),
    ...     ((2, -5), (3, 4), (4, 5)),
    ...     ((-1, 3), (0, 2), (1, 4))))
    (-3, 5, -5, 6)
    """
    def reducer(acc, points):
        xs, ys = tuple(zip(*points))
        return (min(acc[0], min(xs)),
                max(acc[1], max(xs)),
                min(acc[2], min(ys)),
                max(acc[3], max(ys)))

    first = points_list[0]
    xs, ys = tuple(zip(*first))

    return reduce(reducer, points_list[1:],
                  (min(xs), max(xs),
                   min(ys), max(ys)))


def make_plot_descriptor(label, points, style=None):
    """
    Return the descriptor for a series of points
    to be plotted.

    >>> make_plot_descriptor('f(x)', ((1, 2), (3, 4)))
    {'label': 'f(x)', 'points': ((1, 2), (3, 4))}
    """
    return {
        PLOT_LABEL: label,
        PLOT_POINTS: points,
        PLOT_STYLE: style
    }


def make_compound_figure(*descriptors, title=None):
    """
    Make a figure showing multiple functions.

    >>> make_compound_figure(
    ...    make_plot_descriptor('f(x)', ((1, 2), (-3, 4), (5, 6))),
    ...    make_plot_descriptor('g(x)', ((2, -5), (3, 4), (4, 5))),
    ...    make_plot_descriptor('h(x)', ((-1, 3), (0, 2), (1, 4)))
    ... ).show() # doctest: +SKIP
    """
    points_list = tuple(descriptor[PLOT_POINTS] for descriptor in descriptors)
    range_ = get_global_range(points_list)

    figure, axes = plt.subplots()
    if title is not None:
        axes.set_title(title)
    axes.axis(range_)

    for descriptor in descriptors:
        xs, ys = tuple(zip(*descriptor[PLOT_POINTS]))
        if descriptor[PLOT_STYLE] is not None:
            axes.plot(xs, ys, descriptor[PLOT_STYLE], label=descriptor[PLOT_LABEL])
        else:
            axes.plot(xs, ys, label=descriptor[PLOT_LABEL])

    axes.legend()

    return figure
