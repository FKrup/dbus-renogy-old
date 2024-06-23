# dbus-renogy
This application enables communication with Renogy MPPT solar charge controllers. The data is made available on D-Bus, the internal data bus used in Venus OS, allowing for integration with the Venus OS GUI.

## Features
* Communicates with Renogy MPPT solar charge controllers.
* Presents data on D-Bus for seamless integration with Venus OS.
* Allows for monitoring and configuration of charge controller settings via Venus OS GUI.

## Building the Application
To build this application, the following prerequisites are needed:
* A Linux system
* A recent version of QT Creator
* Venus OS SDK
* The proprietary `velib` library (Note: This is not publicly available)

You can find the SDK and instructions for setting up the QT Creator environment here:
[https://github.com/victronenergy/venus/wiki](https://github.com/victronenergy/venus/wiki)

To compile the application:
1. Open the project file `software/dbus-renogy.pro` in QT Creator.
2. Compile the binary following the instructions in the SDK documentation.

## Warning
The repository relies on the `velib` library, which is not publicly accessible.

## Renogy MPPT Compatibility
The application is designed to be compatible with Renogy MPPT solar charge controllers. Specific models and compatibility details should be provided here.

## Development & Toolchain
For local development and testing on a Linux PC:
* Install QT SDK (version 4.8.x) with support for QT D-Bus.
* Run `localsettings` which is available on GitHub: [https://github.com/victronenergy/localsettings](https://github.com/victronenergy/localsettings)

For unit testing, ensure you have a Python interpreter (version 2.7 or newer).

## Architecture
The application consists of the following layers:
* Data acquisition layer
* Data model
* D-Bus integration

Further details on each layer and their components are outlined in the documentation.

## Running Unit Tests
To execute the unit tests, install the required Python interpreter and follow the test execution instructions.

## Contributing
Contributions to improve the application are welcome. Please fork the repository, create your feature branch, commit your changes, push the branch, and then open a pull request.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact
* FKrup
* Project Link: https://github.com/FKrup/dbus-renogy

## Acknowledgments
* Victron Energy for Venus OS and the SDK.
* The maintainers of the `velib` library.
