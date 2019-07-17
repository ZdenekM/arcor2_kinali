# coding: utf-8

"""
    Pick Master Web API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: first
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from arcor2_kinali.swagger_client.models.vec3 import Vec3  # noqa: F401,E501


class Pose6d(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'position': 'Vec3',
        'rotation': 'Vec3'
    }

    attribute_map = {
        'position': 'position',
        'rotation': 'rotation'
    }

    def __init__(self, position=None, rotation=None):  # noqa: E501
        """Pose6d - a model defined in Swagger"""  # noqa: E501

        self._position = None
        self._rotation = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation

    @property
    def position(self):
        """Gets the position of this Pose6d.  # noqa: E501

        Position with coordinates  # noqa: E501

        :return: The position of this Pose6d.  # noqa: E501
        :rtype: Vec3
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Pose6d.

        Position with coordinates  # noqa: E501

        :param position: The position of this Pose6d.  # noqa: E501
        :type: Vec3
        """

        self._position = position

    @property
    def rotation(self):
        """Gets the rotation of this Pose6d.  # noqa: E501

        Rotation in degree  # noqa: E501

        :return: The rotation of this Pose6d.  # noqa: E501
        :rtype: Vec3
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this Pose6d.

        Rotation in degree  # noqa: E501

        :param rotation: The rotation of this Pose6d.  # noqa: E501
        :type: Vec3
        """

        self._rotation = rotation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Pose6d, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Pose6d):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
