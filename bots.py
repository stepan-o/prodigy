import random


def same_dif_bot(f_start, fc1, fc2, p_corr, corr_reward, incorr_reward,
                 corr_frust=-1, incorr_frust=1, max_iter=1000, verbose=False):
    """
    Question-feeding bot that always chooses same difficulty of the question
    :param f_start:
    :param fc1:
    :param fc2:
    :param p_corr:
    :param corr_reward:
    :param incorr_reward:
    :param corr_frust:
    :param incorr_frust:
    :param max_iter:
    :param verbose:
    :return:
    """
    # starting total reward
    r_total = 0
    # starting level of frustration (user-specific)
    f_total = f_start
    for i in range(max_iter):
        # simulate question answer
        if random.random() < p_corr:
            # outcome of successful action
            r_t = corr_reward
            f_total += fc1 * i + corr_frust
        else:
            # outcome of unsuccessful action
            r_t = incorr_reward
            f_total += fc2 * i + incorr_frust
        # add reward
        r_total += r_t
        # check exit condition: frustration under threshold
        if f_total > 1:
            if verbose:
                print("Frustrated! Total questions answered: {0}, total reward = {1:.1f}".format(i, r_total))
            return i, r_total
        else:
            if verbose:
                print("After round {0}, total reward = {1:.1f}, frustration = {2:.2f}, keep playing..."
                      .format(i, r_total, f_total))
    if verbose:
        print("Maximum number of questions reached ({0}), total reward: {1:.1f}".format(max_iter, r_total))
    return max_iter, r_total
