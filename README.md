# CIEPaperFinder [<img align="right" width="160" src="https://i.postimg.cc/DZzkRQtm/README-Icon.png">](https://postimg.cc/FfwBLSFQ)

IMPORTANT: The website the program uses to download papers (GCE Guide) is down, and seemingly permanently so. This means that the program will not work until I find another website or the current website is back online.

CIEPaperFinder is a Python-based graphical user interface (GUI) program that enables users to access and download Cambridge International Examinations (CIE) past papers and resources from a range of 101 IGCSE subjects, 51 O Level subjects, and 81 AS & A Level subjects. Inspired by [CAIE PastPapersOpener](https://github.com/mrc2rules/CAIE_PastPapersOpener) made by [mrc2rules](https://github.com/mrc2rules).

Originally started this because I was bored and I thought the idea was cool. Then decided I might as well put some effort into it. Then I realized this might be plagiarism. Then I realized that's not how plagiarism works. Then I realized it's still kind of a dick move to not bother asking Rahbab. Then I decided, screw it, I'll just release it anyways.

## Using the program

### Downloading and Running

To use the program, all you need to do is download the `CIEPaperFinder.zip` file from the latest release at [Releases](https://github.com/Ali246801232/CIEPaperFinder/releases). All required files and dependencies are included inside of this, so no additional installation is necessary. After downloading, simply extract the directory and execute the `CIEPaperFinder.exe` file inside.

### How to Use

Upon running the program, you will be greeted with this window:

[<img src="https://i.postimg.cc/WzFR1Npv/README-Blank-Window.png" width="271">](https://postimg.cc/ZvSsfhy7)

To download your desired resource, you will need to enter the required information for the resource and then press the "Download File" button. Keep in mind that this program assumes that you have basic knowledge as to how CIE examinations work. Namely how exam sessions work, what subject codes are, how papers are numbered, and what the different types of resources are. In case you're unaware, subject codes are 4-digit numbers that identify a given CIE subject; for example, Chemistry has the code "5054". Additionally, you must input the paper number and variant as a 2-digit number, the first digit being the paper number and the second digit being the variant; for example, paper 2, variant 3 would be "23". The rest of the options are drop-downs so you won't have to worry about formats for those.

### Example Usage

As an example of how to use the program, let's say you want to download the marking scheme for paper 2, variant 2 for O-Level Chemistry (5070) from the examinations held in May/June of 2015. To accomplish this, you would need to enter the following details and then press the "Download File" button:

[<img src="https://i.postimg.cc/LX0KSYpD/README-Filled-Window.png" width="271">](https://postimg.cc/5YvkqtjQ)

After pressing "Download File", a file dialog will be opened where you will have to specify where to download the file. By default, this is set to the Downloads folder but you can browse for an exact location if you wish:

[<img src="https://i.postimg.cc/c12y5nT4/README-Save-As-Window.png" width="348">](https://postimg.cc/hhL5XhHH)

Your paper should be saved in the location you specified in the file dialog and you can navigate to the it to confirm. Keep in mind that files may take a while to appear in the specified location depending on your internet speed:

[<img src="https://i.postimg.cc/HnfqJqj7/README-Downloaded-File.png" width="348">](https://postimg.cc/FkVW8ny9)

## Reporting Bugs or Issues

If you encounter any problems while using CIEPaperFinder, well gl because I keep forgetting I made this thing, but here's some guidelines anyways:

1. Check the [Changelog](https://github.com/Ali246801232/CIEPaperFinder/blob/main/README.md#changelog) section to see if the issue has already been fixed in a newer version of the program.
2. Search the existing [Issues](https://github.com/Ali246801232/CIEPaperFinder/issues) to see if the problem has already been reported by someone else.
3. If the issue has not been resolved or reported, open a new issue by going to the "[Issues](https://github.com/Ali246801232/CIEPaperFinder/issues)" tab, and then clicking the "[New Issue](https://github.com/Ali246801232/CIEPaperFinder/issues/new/choose)" button.
4. Provide a clear and descriptive title for the issue, and include the following information in the description:
   - How to reproduce the problem.
   - The expected outcome and the actual outcome.
   - The version of the program you are using (found in the [Changelog](https://github.com/Ali246801232/CIEPaperFinder/blob/main/README.md#changelog)).
   - Any error message that appears.
   - Screenshots or any other relevant information that might help solve the problem.

Before reporting an issue, please make sure that it is not related to the following known issues:

- Specimen papers are not supported as their file format is too different from those of past papers. This is solvable and will probably be a feature in future version (if that ever happens) but, for now, you cannot download resources related to specimen papers.
- Some subjects or resources are not supported. The website used to find and download files does not have papers uploaded for every subject and examination. As this is an issue with the website, if a subject or resource is missing, you will unfortunately have to spend time looking for a different source online yourself.
- Some files exist on the website but can't be found. The website used has a defined naming convention for its files which is used to find them. However, some files don't follow this and, as a result, cannot be found. As this is an issue with the website, if you come across such a file, you will unfortunately have to spend time looking for it online yourself.

## License

This project is licensed under the terms of the MIT License. A copy of the license can be found in the [LICENSE](LICENSE) file.

## Changelog

### Version 0.1.0 (2023-04-01)
- Initial pre-release of the program
