# How to add a Qt kit to PATH

In this guide, I show you how to add a Qt kit to your PATH environment variable.

# Requirements

You need to have downloaded and installed:

1. Qt 5.15.

In this guide, I have installed Qt into the default directory: "C:\Qt".

# Steps

Follow the below steps to add the MinGW kit to the PATH environment variable.

## Step 1

Either:

1. Left click on the Start menu icon.
1. Scroll down to "Control Panel".
1. Left click on the icon.

Or:

1. Press the <kbd>WINDOWS</kbd> key.
1. Type the string "Control Panel".
1. Press the <kbd>Enter</kbd> key.

When done, you should see a window similar to the following:

![Control Panel](images/01_control_panel.png)

## Step 2

Left click on the "System" icon.

When done, you should see a window similar to the following:

![System](images/02_system.png)

## Step 3

Left click on "Advanced system settings" link.

When done, you should see a window similar to the following:

![System Properties](images/03_system_properties.png)

## Step 4

Left click on "Environment Variables".

When done, you should see a window similar to the following:

![Environment Variables](images/04_environment_variables.png)

## Step 5

Left click on "System Variables"'s "Path" variable.

Left click on the "Edit" button.

When done, you should see a window similar to the following:

![Path](images/05_path.png)

## Step 6

Left click on the "Browse" button.

When done, you should see a window similar to the following:

![Browse](images/06_browse.png)

## Step 7

Browse to the following directory:

```Console
C:\Qt\5.15\mingw81_64\bin
```
Left click on the "OK" button. This will add the above path to your PATH environment variable.

**Note**: If you installed additional kits during Qt Creator's installation, you should add their corresponding directories to PATH, e.g. if you installed the MSVC 2019 64-bit kit, you should add "C:\Qt\5.15\msvc2019_64\bin" to PATH.

## Step 8

Left click on the "Browse" button.

When done, you should see a window similar to the following:

![Browse](images/06_browse.png)

## Step 9

Browse to the following directory:

```Console
C:\Qt\Tools\mingw810_64\bin
```

Left click on the "OK" button. This will add the above path to your PATH environment variable.

## Step 10

Left click on each windows' "Cancel" or close button.

# Conclusion

If you've followed these steps correctly, you have added a Qt kit to your PATH environment variable.

# Credit

Dr Frazer K. Noble  
Department of Mechanical and Electrical Engineering  
Massey University  
Auckland  
New Zealand  