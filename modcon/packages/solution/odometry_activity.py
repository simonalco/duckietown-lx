from typing import Tuple

import numpy as np


def delta_phi(ticks: int, prev_ticks: int, resolution: int) -> Tuple[float, float]:
    """
    Args:
        ticks: Current tick count from the encoders.
        prev_ticks: Previous tick count from the encoders.
        resolution: Number of ticks per full wheel rotation returned by the encoder.
    Return:
        rotation_wheel: Rotation of the wheel in radians.
        ticks: current number of ticks.
    """

    d_ticks = ticks - prev_ticks
    dphi = 2*np.pi*d_ticks/resolution

    return dphi, d_ticks


def pose_estimation(
    R: float,
    baseline: float,
    x_prev: float,
    y_prev: float,
    theta_prev: float,
    delta_phi_left: float,
    delta_phi_right: float,
) -> Tuple[float, float, float]:

    """
    Calculate the current Duckiebot pose using the dead-reckoning model.

    Args:
        R:                  radius of wheel (both wheels are assumed to have the same size) - this is fixed in simulation,
                            and will be imported from your saved calibration for the real robot
        baseline:           distance from wheel to wheel; 2L of the theory
        x_prev:             previous x estimate - assume given
        y_prev:             previous y estimate - assume given
        theta_prev:         previous orientation estimate - assume given
        delta_phi_left:     left wheel rotation (rad)
        delta_phi_right:    right wheel rotation (rad)

    Return:
        x:                  estimated x coordinate
        y:                  estimated y coordinate
        theta:              estimated heading
    """

    d_left = R*delta_phi_left       # distance travelled by left wheel in meters
    d_right = R*delta_phi_right       # distance travelled by right wheel in meters

    d_A = (d_left + d_right)/2
    d_theta = (d_right - d_left)/baseline

    theta_curr = theta_prev + d_theta
    x_curr = x_prev + d_A*np.cos(theta_curr)
    y_curr = y_prev + d_A*np.sin(theta_curr)

    return x_curr, y_curr, theta_curr
