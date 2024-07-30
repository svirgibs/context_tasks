class Applicant:
    def __init__(self, idx: int, checked: bool = False):
        self.idx = idx,
        self.checked = checked

    def __repr__(self):
        return repr(self.idx[0])


def counting_rhyme(applicants_value: int, tacts_value: int):
    applicants = [Applicant(x + 1) for x in range(applicants_value)]

    tact = 1

    while len(applicants) > 1:
        applicants_temp = applicants.copy()
        for applicant in applicants_temp:
            if applicant.checked is True:
                applicants.append(applicant)
                applicant.checked = False
                del applicants[0]

        for index, applicant in enumerate(applicants):
            applicant.checked = True
            if tact == tacts_value:
                applicants.pop(index)
                tact = 1
                break
            tact += 1

    return applicants[0].idx[0]


if __name__ == '__main__':
    with open('input.txt') as file_input:
        applicants = int(file_input.readline().rstrip())
        tacts = int(file_input.readline().rstrip())

    result = counting_rhyme(applicants, tacts)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
